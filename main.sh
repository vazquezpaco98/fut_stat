#!/bin/bash
if [ -f "resultados.json" ]; then
    rm resultados.json;
fi
python3 main.py >> resultados.json;