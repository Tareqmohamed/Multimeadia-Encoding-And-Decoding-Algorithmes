import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from scipy.fftpack import dct, idct

class JPEGApp:
    def __init__(self, master):
        self.master = master
        master.title("JPEG Compression/Decompression")

        self.image_label = tk.Label(master, text="Original Image:")
        self.image_label.pack()

        self.canvas_original = tk.Canvas(master)
        self.canvas_original.pack()

        self.load_button = tk.Button(master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.compress_button = tk.Button(master, text="Compress", command=self.compress_image)
        self.compress_button.pack()

        self.decompress_button = tk.Button(master, text="Decompress", command=self.decompress_image)
        self.decompress_button.pack()

        self.compressed_image_label = tk.Label(master, text="Compressed Image:")
        self.compressed_image_label.pack()

        self.canvas_compressed = tk.Canvas(master)
        self.canvas_compressed.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.display_image(self.original_image, self.canvas_original)

    def compress_image(self):
        if hasattr(self, 'original_image'):
            compressed_image = self.compress_jpeg(np.array(self.original_image))
            compressed_image_pil = Image.fromarray(compressed_image.astype(np.uint8))
            self.display_image(compressed_image_pil, self.canvas_compressed)

    def decompress_image(self):
        if hasattr(self, 'original_image'):
            compressed_image = self.compress_jpeg(np.array(self.original_image))
            decompressed_image = self.decompress_jpeg(compressed_image)
            decompressed_image_pil = Image.fromarray(decompressed_image.astype(np.uint8))
            self.display_image(decompressed_image_pil, self.canvas_compressed)

    def compress_jpeg(self, image):
        # This is a simplified compression
        # Replace this with your actual JPEG compression logic
        # The example here just scales down the image by a factor
        scale_factor = 0.5
        compressed_image = np.round(image * scale_factor).astype(np.uint8)
        return compressed_image

    def decompress_jpeg(self, compressed_image):
        # This is a simplified decompression
        # Replace this with your actual JPEG decompression logic
        # The example here just scales up the compressed image by the inverse factor
        inverse_scale_factor = 2.0
        decompressed_image = np.round(compressed_image * inverse_scale_factor).astype(np.uint8)
        return decompressed_image

    def display_image(self, image, canvas):
        photo = ImageTk.PhotoImage(image)
        canvas.config(width=image.width, height=image.height)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = JPEGApp(root)
    root.mainloop()
