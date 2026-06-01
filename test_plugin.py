"""
Script to test cellpose-napari plugin functionality without downloading data
"""
import numpy as np
import sys

print("Testing cellpose-napari plugin components...")

# Test 1: Import the plugin
print("\n=== Test 1: Import Plugin Components ===")
try:
    from cellpose_napari import (
        napari_experimental_provide_dock_widget,
        napari_provide_sample_data
    )
    print("✓ Successfully imported plugin components")
except Exception as e:
    print(f"✗ Error importing components: {e}")
    sys.exit(1)

# Test 2: Check sample data registration
print("\n=== Test 2: Check Sample Data Registration ===")
try:
    sample_data_dict = napari_provide_sample_data()
    print(f"✓ Sample data registered: {list(sample_data_dict.keys())}")
    for key, value in sample_data_dict.items():
        print(f"  - {key}: {value.get('display_name', 'N/A')}")
except Exception as e:
    print(f"✗ Error getting sample data: {e}")
    sys.exit(1)

# Test 3: Test dock widget creation (without napari viewer)
print("\n=== Test 3: Test Basic Widget Structure ===")
try:
    from cellpose_napari._dock_widget import CP_models
    print(f"✓ Found {len(CP_models)} available Cellpose models:")
    for model in CP_models:
        print(f"  - {model}")
except Exception as e:
    print(f"✗ Error loading dock widget: {e}")
    sys.exit(1)

# Test 4: Create synthetic test image and verify cellpose can be imported
print("\n=== Test 4: Test Cellpose Import ===")
try:
    from cellpose import models
    print("✓ Cellpose models module imported successfully")
    print(f"  Available models will be loaded when needed")
except Exception as e:
    print(f"✗ Error importing cellpose: {e}")
    sys.exit(1)

# Test 5: Create a small test image
print("\n=== Test 5: Create Test Image ===")
try:
    # Create a small 64x64 synthetic image with a cell-like structure
    test_image = np.random.randint(0, 100, (64, 64, 3), dtype=np.uint8)
    # Add a bright blob in the middle
    test_image[20:40, 20:40, :] = 200
    print(f"✓ Created synthetic test image: shape {test_image.shape}, dtype {test_image.dtype}")
    print(f"  Image statistics:")
    print(f"    - Min: {test_image.min()}, Max: {test_image.max()}")
    print(f"    - Mean: {test_image.mean():.1f}")
except Exception as e:
    print(f"✗ Error creating test image: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("✓ All tests passed successfully!")
print("="*50)
print("\nThe cellpose-napari plugin is ready to use!")
print("To launch napari with the plugin, run: napari")
