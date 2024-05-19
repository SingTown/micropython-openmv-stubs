set -e
tag=$1
rm -rf repos
mkdir -p repos/micropython-stubs/stubs
(
    cd repos
    git clone https://github.com/openmv/micropython.git
    cd micropython
    git checkout $tag
)
(
    cd repos/micropython/docs/library
    for file in omv.*.rst; do
        ln -s -- "$file" "${file#omv.}"
    done
)