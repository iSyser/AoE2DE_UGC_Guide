$env:PYTHONPATH = ([string](Get-Location) + "./scripts/python;")
Push-Location "./docs/general/xs/constants"
python  functions.py
Pop-Location
