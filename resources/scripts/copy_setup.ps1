# Full path of the file
$file = 'setup.py'
$ProjectName = "psycopg2-helper"
$ProjectVersion = "0.1.5"

# remove the file if it exists
if (Test-Path -Path $file -PathType Leaf) {
    Remove-Item $file
}

Push-Location dist
tar -xf ".\$ProjectName-$ProjectVersion.tar.gz"
Move-Item ".\$ProjectName-$ProjectVersion\setup.py" ../.
Remove-Item "$ProjectName-$ProjectVersion" -Recurse
Pop-Location
