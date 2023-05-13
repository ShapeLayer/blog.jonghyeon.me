if [ -d "customizer" ]; then
    rm -rf customizer
fi
git clone https://github.com/ShapeLayer/customizer-jekyll-chirpy.git customizer
cd customizer
sh app.sh
