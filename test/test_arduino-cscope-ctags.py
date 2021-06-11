#!/bin/python3

import subprocess
from pathlib import Path
import shutil
import importlib
import sys

# Helper function to load python module from file name
def import_from_path(path):
    module_name = Path(path).name.replace('-', '_')
    spec = importlib.util.spec_from_loader(
        module_name,
        importlib.machinery.SourceFileLoader(module_name, path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module

# Instanced the main object
ccino = import_from_path("./arduino-cscope-ctags")

test_sketch_path = Path("./test/FreeRTOS_ESP32").absolute()

def test_main_default():
  ccino.main(
    "esp32:esp32:nodemcu-32s",
    str(test_sketch_path),
    ".tags"
  )

  tags_path = test_sketch_path/".tags"

  assert tags_path.is_dir()
  assert (tags_path/"cscope.out").is_file()
  assert (tags_path/"cscope.in.out").is_file()
  assert (tags_path/"cscope.po.out").is_file()
  assert (tags_path/"ctags").is_file()

  # Clean up
  shutil.rmtree(tags_path)

def test_main_custom_output():
  ccino.main(
    "esp32:esp32:nodemcu-32s",
    str(test_sketch_path),
    ".tags/custom/"
  )

  tags_path = test_sketch_path/".tags/custom"

  assert tags_path.is_dir()
  assert (tags_path/"cscope.out").is_file()
  assert (tags_path/"cscope.in.out").is_file()
  assert (tags_path/"cscope.po.out").is_file()
  assert (tags_path/"ctags").is_file()

  # Clean up
  shutil.rmtree(test_sketch_path/".tags")