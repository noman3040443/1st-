import replicate

output = replicate.run(
  "stability-ai/stable-diffusion-3",
  input={
    "prompt": "a photo of vibrant artistic graffiti on a wall saying \"SD3 medium\""
  }
)

print(output)