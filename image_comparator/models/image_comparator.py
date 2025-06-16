from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
from PIL import Image
import io
import imagehash
import logging

_logger = logging.getLogger(__name__)

class ImageComparator(models.Model):
    _name = 'image.comparator'
    _description = 'Image Comparator'

    name = fields.Char(string="Nom")
    image_reference = fields.Binary(string="Image de référence", attachment=True)
    image_uploaded = fields.Binary(string="Image téléversée", attachment=True)
    similarity_score = fields.Float(string="Score de similarité", readonly=True)
    gallery_ids = fields.Many2many('image.gallery', string="Images de la galerie")
    gallery_results = fields.One2many('image.comparison.result', 'comparator_id', string="Résultats")

    def _prepare_image(self, binary_data):
        """Convert binary data to PIL Image."""
        try:
            image_stream = io.BytesIO(base64.b64decode(binary_data))
            return Image.open(image_stream).convert('RGB')
        except Exception as e:
            raise UserError(f"Erreur lors de la préparation de l'image: {str(e)}")

    def compare_images(self):
        """Compare two images using perceptual hashing."""
        try:
            # Get PIL images
            img1 = self._prepare_image(self.image_reference)
            img2 = self._prepare_image(self.image_uploaded)

            # Calculate perceptual hashes
            hash1 = imagehash.average_hash(img1, hash_size=8)
            hash2 = imagehash.average_hash(img2, hash_size=8)

            # Calculate Hamming distance (number of different bits)
            difference = float(hash1 - hash2)

            # Convert to percentage similarity (0-100)
            similarity = (1 - (difference / 64.0)) * 100.0
            
            # Round to 2 decimal places and ensure between 0-100
            self.similarity_score = round(max(0.0, min(100.0, similarity)), 2)

        except Exception as e:
            self.similarity_score = 0.0
            raise UserError(f"Erreur lors de la comparaison des images: {str(e)}")
        
    def compare_with_gallery(self):
        """Compare uploaded image with all gallery images."""
        self.ensure_one()
        
        # Delete old results
        self.gallery_results.unlink()
        
        if not self.image_uploaded:
            raise UserError("Veuillez d'abord téléverser une image à comparer")
        
        # Get the uploaded image hash once
        img_uploaded = self._prepare_image(self.image_uploaded)
        hash_uploaded = imagehash.average_hash(img_uploaded, hash_size=8)
        
        # Compare with each gallery image
        for gallery_image in self.gallery_ids:
            try:
                # Prepare gallery image
                img_gallery = self._prepare_image(gallery_image.image)
                hash_gallery = imagehash.average_hash(img_gallery, hash_size=8)
                
                # Calculate similarity
                difference = float(hash_gallery - hash_uploaded)
                similarity = (1 - (difference / 64.0)) * 100.0
                score = round(max(0.0, min(100.0, similarity)), 2)
                
                # Create result record
                self.env['image.comparison.result'].create({
                    'comparator_id': self.id,
                    'gallery_image_id': gallery_image.id,
                    'similarity_score': score
                })
                
            except Exception as e:
                # Log error but continue with other images
                _logger.error(f"Erreur lors de la comparaison avec l'image {gallery_image.name}: {str(e)}")
                continue
        
        return True
