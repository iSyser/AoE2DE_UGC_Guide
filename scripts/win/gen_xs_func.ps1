$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/general/xs/functions"
python functions.py
Pop-Location
