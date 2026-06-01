"""
Script to run sample data from cellpose-napari plugin
"""
import sys
from cellpose_napari._sample_data import rgb_3D, rgb_2D

print("Loading sample data...")

# Load 2D sample data
print("\n=== Loading 2D Sample Data ===")
try:
    data_2d = rgb_2D()
    print(f"2D data loaded successfully!")
    print(f"  Type: {type(data_2d)}")
    print(f"  Length: {len(data_2d)}")
    if len(data_2d) > 0:
        image_data, metadata = data_2d[0]
        print(f"  Image shape: {image_data.shape}")
        print(f"  Image dtype: {image_data.dtype}")
        print(f"  Metadata: {metadata}")
except Exception as e:
    print(f"Error loading 2D data: {e}")
    import traceback
    traceback.print_exc()

# Load 3D sample data
print("\n=== Loading 3D Sample Data ===")
try:
    data_3d = rgb_3D()
    print(f"3D data loaded successfully!")
    print(f"  Type: {type(data_3d)}")
    print(f"  Length: {len(data_3d)}")
    if len(data_3d) > 0:
        image_data, metadata = data_3d[0]
        print(f"  Image shape: {image_data.shape}")
        print(f"  Image dtype: {image_data.dtype}")
        print(f"  Metadata: {metadata}")
except Exception as e:
    print(f"Error loading 3D data: {e}")
    import traceback
    traceback.print_exc()

print("\n✓ Sample data loading test complete!")
