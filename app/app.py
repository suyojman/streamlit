import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from src.visualize import DataVisualization
#"""
#This is main file to run the application
#"""

if __name__ == '__main__':
    dvs = DataVisualization()
    dvs.show_data()