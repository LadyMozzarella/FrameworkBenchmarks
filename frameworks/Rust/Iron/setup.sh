#!/bin/bash

sed -i 's|localhost|'"${DBHOST}"'|g' src/main.rs

cargo build --release
cargo run -v --release &
