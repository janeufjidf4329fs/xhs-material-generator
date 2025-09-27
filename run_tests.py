
import argparse
import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from scripts.generator import generate_images
from scripts.image_comparator import create_diff_report

def main():
    parser = argparse.ArgumentParser(description='Run image generation and comparison tests.')
    parser.add_argument('--reference-dir', default='references', help='Directory with reference images.')
    parser.add_argument('--output-dir', default='output/images', help='Directory to save generated images.')
    parser.add_argument('--report-path', default='report.md', help='Path to save the diff report.')
    parser.add_argument('--similarity-threshold', type=float, default=95.0, help='Similarity threshold for passing the test.')
    parser.add_argument('--texts', nargs='+', default=['Text 1', 'Text 2', 'Text 3', 'Text 4'], help='List of texts to generate images for.')

    args = parser.parse_args()

    # Generate images
    print(f"Generating images to {args.output_dir}...")
    generate_images(args.texts, args.output_dir)
    print("Image generation complete.")

    # Create diff report
    print(f"Creating diff report at {args.report_path}...")
    create_diff_report(args.report_path, args.reference_dir, args.output_dir, args.similarity_threshold)
    print("Diff report complete.")

if __name__ == '__main__':
    main()
