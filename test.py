import math
import os
import unittest

import bpy
import debugpy

debugpy.listen(("0.0.0.0", 6000))
print("debugpy version is: " + debugpy.__version__)
print("Waiting")
debugpy.wait_for_client()
print("Connected")
input('Press Enter to Exit')


class TestBlenderScript(unittest.TestCase):
    def test_file_paths_and_image_loading(self):
        # Test STL and image file paths
        self.assertTrue(os.path.exists(stl_path))
        self.assertTrue(os.path.exists(image_path))

        # Test image loading
        image = bpy.data.images.get('image.png')
        self.assertIsNotNone(image)

    def test_scene_setup(self):
        # Test camera and light creation
        self.assertEqual(len(bpy.data.objects), 2)
        self.assertIsInstance(bpy.context.scene.camera, bpy.types.Camera)

    def test_mesh_import_and_material(self):
        # Test mesh import and material assignment
        self.assertEqual(len(bpy.data.objects), 3)
        self.assertIsInstance(cola_obj.data.materials[0], bpy.types.Material)

    # ... other test methods ...


if __name__ == '__main__':
    # Set up paths and other variables here
    stl_path = "/Users/admin/Blender/Tutorial/Cola.stl"
    image_path = "/Users/admin/Blender/Tutorial/image.png"

    # Run the tests
    unittest.main()
