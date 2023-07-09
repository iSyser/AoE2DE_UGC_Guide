$env:PYTHONPATH=([string](Get-Location) + "./docs/assets/python;")
Push-Location "docs/general/attributes"
python attributes.py
Pop-Location
