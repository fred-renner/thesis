from PIL import Image, ImageSequence

def slow_down_gif(input_path, output_path, slowdown_factor):
    # Open the input GIF
    with Image.open(input_path) as img:
        # Extract frames and slow them down
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        slowed_frames = [frame.copy() for frame in frames]
        for frame in slowed_frames:
            frame.info['duration'] *= slowdown_factor

        # Save the new GIF
        slowed_frames[0].save(output_path, save_all=True, append_images=slowed_frames[1:], loop=0)

# Example usage
slow_down_gif('/Users/fred/Downloads/animation.gif', '/Users/fred/Downloads/blah.gif', 10) # Slow down by a factor of 2

