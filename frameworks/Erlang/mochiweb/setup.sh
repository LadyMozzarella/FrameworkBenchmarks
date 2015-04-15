#!/bin/bash

source $IROOT/erlang.installed
source $IROOT/rebar.installed

sed -i 's|{db_host, \".*\"}|{db_host, \""'$DBHOST'"\"}|g' priv/app.config

./rebar clean get-deps compile
erl +K true +sbwt very_long +swt very_low -pa ebin deps/*/ebin -boot start_sasl -config priv/app.config -s mochiweb_bench_app
