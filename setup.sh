pip install -v -e .
pip install torch==2.4.1 torchvision xformers huggingface_hub==0.25.0 wat-inspector codetiming flops_profiler flash-attn
sed -i 's/if use_kernel/if False/' opensora/models/layers/blocks.py
sed -i 's/fmha.BlockDiagonalMask/fmha.attn_bias.BlockDiagonalMask/' opensora/models/layers/blocks.py