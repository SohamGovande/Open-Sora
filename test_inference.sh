# text to video
python scripts/inference.py configs/opensora-v1-2/inference/sample.py \
  --num-frames 2s --resolution 240p --aspect-ratio 9:16 \
  --prompt "a beautiful waterfall" 
  #> flops.txt 2>&1