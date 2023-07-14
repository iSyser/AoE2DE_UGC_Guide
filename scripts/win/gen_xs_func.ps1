$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/xs/functions"
python functions.py
Pop-Location
