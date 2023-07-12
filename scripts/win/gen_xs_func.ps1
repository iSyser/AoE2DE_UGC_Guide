$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/general/xs"
python functions.py
Pop-Location
