#!/usr/bin/env python
"""
Test script for mlp_personal_style package

This script tests and demonstrates the functionality of the mlp_personal_style package
by creating various plot types with both light and dark styles.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from mlp_personal_style import light, dark

# Create output directory if it doesn't exist
OUTPUT_DIR = "test_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_sample_data():
    """Generate sample data for testing plots."""
    # Generate x values
    x = np.linspace(0, 10, 100)
    
    # Generate various y values for different plots
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)
    y_exp = np.exp(0.1 * x)
    
    # Random data for scatter plots
    x_scatter = np.random.rand(50) * 10
    y_scatter = np.random.rand(50) * 5
    
    # Categories for bar charts
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.rand(5) * 10
    
    return {
        'x': x,
        'y_sin': y_sin,
        'y_cos': y_cos,
        'y_tan': y_tan,
        'y_exp': y_exp,
        'x_scatter': x_scatter,
        'y_scatter': y_scatter,
        'categories': categories,
        'values': values
    }

def create_line_plot(data, style_name, style_path):
    """Create and save a line plot with the specified style."""
    plt.style.use(style_path)
    
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y_sin'], label='sin(x)')
    ax.plot(data['x'], data['y_cos'], label='cos(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Line Plot with {style_name} Style')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/line_plot_{style_name}.png")
    plt.close()

def create_scatter_plot(data, style_name, style_path):
    """Create and save a scatter plot with the specified style."""
    plt.style.use(style_path)
    
    fig, ax = plt.subplots()
    ax.scatter(data['x_scatter'], data['y_scatter'], alpha=0.7, s=50)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Scatter Plot with {style_name} Style')
    
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/scatter_plot_{style_name}.png")
    plt.close()

def create_bar_plot(data, style_name, style_path):
    """Create and save a bar plot with the specified style."""
    plt.style.use(style_path)
    
    fig, ax = plt.subplots()
    ax.bar(data['categories'], data['values'])
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_title(f'Bar Plot with {style_name} Style')
    
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/bar_plot_{style_name}.png")
    plt.close()

def create_histogram(data, style_name, style_path):
    """Create and save a histogram with the specified style."""
    plt.style.use(style_path)
    
    fig, ax = plt.subplots()
    ax.hist(data['y_sin'], bins=20, alpha=0.7)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram with {style_name} Style')
    
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/histogram_{style_name}.png")
    plt.close()

def create_subplot_figure(data, style_name, style_path):
    """Create and save a figure with subplots using the specified style."""
    plt.style.use(style_path)
    
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    
    # Line plot
    axs[0, 0].plot(data['x'], data['y_sin'])
    axs[0, 0].set_title('Sine Wave')
    
    # Scatter plot
    axs[0, 1].scatter(data['x_scatter'], data['y_scatter'], alpha=0.7)
    axs[0, 1].set_title('Scatter Plot')
    
    # Bar plot
    axs[1, 0].bar(data['categories'], data['values'])
    axs[1, 0].set_title('Bar Plot')
    
    # Histogram
    axs[1, 1].hist(data['y_sin'], bins=20)
    axs[1, 1].set_title('Histogram')
    
    plt.suptitle(f'Multiple Plot Types with {style_name} Style')
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/subplots_{style_name}.png")
    plt.close()

def test_context_manager(data):
    """Test the context manager functionality of the styles."""
    # Default style
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y_sin'])
    ax.set_title('Default Style')
    plt.savefig(f"{OUTPUT_DIR}/context_default.png")
    plt.close()
    
    # Using light style with context manager
    with plt.style.context(light.incredible_style):
        fig, ax = plt.subplots()
        ax.plot(data['x'], data['y_sin'])
        ax.set_title('Light Style (Context Manager)')
        plt.savefig(f"{OUTPUT_DIR}/context_light.png")
    plt.close()
    
    # Using dark style with context manager
    with plt.style.context(dark.incredible_style):
        fig, ax = plt.subplots()
        ax.plot(data['x'], data['y_sin'])
        ax.set_title('Dark Style (Context Manager)')
        plt.savefig(f"{OUTPUT_DIR}/context_dark.png")
    plt.close()
    
    # Verify we're back to default style
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y_sin'])
    ax.set_title('Back to Default Style')
    plt.savefig(f"{OUTPUT_DIR}/context_after.png")
    plt.close()

def test_light_style(data):
    """Test all plot types with the light style."""
    print("Testing light style...")
    create_line_plot(data, 'light', light.incredible_style)
    create_scatter_plot(data, 'light', light.incredible_style)
    create_bar_plot(data, 'light', light.incredible_style)
    create_histogram(data, 'light', light.incredible_style)
    create_subplot_figure(data, 'light', light.incredible_style)
    print("Light style tests completed.")

def test_dark_style(data):
    """Test all plot types with the dark style."""
    print("Testing dark style...")
    create_line_plot(data, 'dark', dark.incredible_style)
    create_scatter_plot(data, 'dark', dark.incredible_style)
    create_bar_plot(data, 'dark', dark.incredible_style)
    create_histogram(data, 'dark', dark.incredible_style)
    create_subplot_figure(data, 'dark', dark.incredible_style)
    print("Dark style tests completed.")

def run_all_tests():
    """Run all tests for the mlp_personal_style package."""
    print(f"Testing mlp_personal_style package...")
    print(f"Output directory: {os.path.abspath(OUTPUT_DIR)}")
    
    # Generate sample data
    data = generate_sample_data()
    
    # Test both styles
    test_light_style(data)
    test_dark_style(data)
    
    # Test context manager functionality
    print("Testing style context manager...")
    test_context_manager(data)
    print("Context manager tests completed.")
    
    print(f"All tests completed. Results saved to {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    run_all_tests()