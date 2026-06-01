"""
Simple test to verify cellpose is working
"""
import numpy as np

print("Testing basic cellpose functionality...")

# Test 1: Import cellpose
print("\n=== Test 1: Import Cellpose ===")
try:
    from cellpose import models
    print("✓ Cellpose imported successfully")
except Exception as e:
    print(f"✗ Error: {e}")
    import sys
    sys.exit(1)

# Test 2: Create synthetic test image
print("\n=== Test 2: Create Synthetic Test Image ===")
test_image = np.random.randint(50, 150, (128, 128, 3), dtype=np.uint8)
# Add some bright regions to simulate cells
for _ in range(5):
    y, x = np.random.randint(20, 100, 2)
    test_image[y:y+30, x:x+30, :] = 220
print(f"✓ Created test image: shape {test_image.shape}, dtype {test_image.dtype}")

# Test 3: Try loading a model
print("\n=== Test 3: Load Cellpose Model ===")
try:
    print("  Loading 'cyto3' model...")
    model = models.CellposeModel(model_type='cyto3', gpu=True)
    print("✓ Cellpose model loaded successfully")
    
    # Test 4: Run inference on small image
    print("\n=== Test 4: Run Cellpose Inference ===")
    print("  Running segmentation on test image...")
    channels = [0, 0]  # [cytoplasm, nuclei] - using grayscale for both
    masks, flows, styles = model.eval(test_image, channels=channels, diameter=30)
    print(f"✓ Inference completed successfully")
    print(f"  Output masks shape: {masks.shape}")
    print(f"  Number of cells detected: {len(np.unique(masks)) - 1}")  # -1 for background
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    import sys
    sys.exit(1)

print("\n" + "="*50)
print("✓ All tests passed!")
print("="*50)
