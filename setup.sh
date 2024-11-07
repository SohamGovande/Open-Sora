pip install -v -e .
pip install torch==2.4.1 torchvision xformers huggingface_hub==0.25.0 wat-inspector codetiming flops_profiler flash-attn
sed -i 's/if use_kernel/if False/' opensora/models/layers/blocks.py
sed -i 's/fmha.BlockDiagonalMask/fmha.attn_bias.BlockDiagonalMask/' opensora/models/layers/blocks.py

ROTARY_FILE=$(python3 -c "import rotary_embedding_torch.rotary_embedding_torch as rotary_embedding_torch; print(rotary_embedding_torch.__file__)")
sed -i "s/if False: self.register_buffer/self.register_buffer/" "$ROTARY_FILE"
sed -i "s/self.register_buffer/if False: self.register_buffer/" "$ROTARY_FILE"
