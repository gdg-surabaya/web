#!/bin/bash
cd "${0%/*}"
gunicorn app:app -b 0.0.0.0:8000 &