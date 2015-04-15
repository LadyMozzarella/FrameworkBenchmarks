#!/bin/bash

RUST_VERSION="1.0.0-beta"

RETCODE=$(fw_exists rust-$RUST_VERSION.installed)
[ ! "$RETCODE" == 0 ] || { return 0; }

fw_get https://static.rust-lang.org/dist/rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz
fw_untar rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz

mv rust-$RUST_VERSION-x86_64-unknown-linux-gnu rust-$RUST_VERSION
cd rust-$RUST_VERSION

sudo ./install.sh

echo "export RUST_HOME=$IROOT/rust-$RUST_VERSION" > $IROOT/rust-$RUST_VERSION.installed
echo "export LD_LIBRARY_PATH=$MONO_HOME/lib:$LD_LIBRARY_PATH" >> $IROOT/rust-$RUST_VERSION.installed
