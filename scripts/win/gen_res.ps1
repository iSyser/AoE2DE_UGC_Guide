$env:PYTHONPATH=([string](Get-Location) + "./docs/assets/python;")
Push-Location "docs/general/resources"
python resources.py
Pop-Location
