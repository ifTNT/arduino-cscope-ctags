#!/bin/bash

if [ "$TRAVIS_OS_NAME" = "osx" ]; then
  brew update
  brew install arduino-cli ctags cscope
fi

if [ "$TRAVIS_OS_NAME" = "linux" ]; then
  sudo apt-get update
  # Cscope and ctags
  sudo apt install cscope exuberant-ctags
  # Latest version of arduino-cli
  mkdir -p ${HOME}/local/bin
  curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=${HOME}/local/bin sh
fi

# Install arduino-esp32 for testing
arduino-cli core install --additional-urls https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json esp32:esp32@1.0.6