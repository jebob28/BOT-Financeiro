$exclude = @("venv", "Financeiro.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Financeiro.zip" -Force