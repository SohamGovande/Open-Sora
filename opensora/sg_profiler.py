import torch.profiler
import time
import os
from opensora.soham.config import SHOULD_PROFILE

def on_trace_ready(prof, prefix=""):
  trace_path = f"/scr/govande/opensora/torchlog/opensora/trace-{prefix}-{int(time.time() * 1000)}"
  print(f"Attempting to export trace to {trace_path}")
  prof.export_chrome_trace(trace_path + ".json")
  print('Exported trace file')
  print(prof.key_averages().table(sort_by="self_cpu_time_total", row_limit=10))

def do_nothing(*args, **kwargs):
  pass

def sg_profiler(prefix=""):
  return torch.profiler.profile(
    schedule=torch.profiler.schedule(wait=2, warmup=2, active=1),
    # on_trace_ready=torch.profiler.tensorboard_trace_handler(f"/scr/govande/opensora/torchlog/opensora_tb/{prefix}"),
    on_trace_ready=(lambda prof: on_trace_ready(prof, prefix)) if SHOULD_PROFILE else do_nothing,
    record_shapes=True,
    profile_memory=True,
    with_flops=True,
    with_modules=True,
    with_stack=True
  )