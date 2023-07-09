$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/general/attributes"
python attributes.py
Pop-Location
