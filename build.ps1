$exclude = @("venv", "bot_climamanaus.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_climamanaus.zip" -Force