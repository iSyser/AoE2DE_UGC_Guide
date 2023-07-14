$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/xs/constants"
python constants.py
Pop-Location
