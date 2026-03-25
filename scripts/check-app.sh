#!/bin/bash
# Script de monitoreo simple para verificar el estado de la aplicación

echo "🔍 Verificando aplicación..."
echo "=============================="

# Verificar ping
echo -n "Ping: "
if curl -f http://localhost:80/ping > /dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ FAIL"
fi

# Verificar health
echo -n "Health: "
if curl -f http://localhost:80/health > /dev/null 2>&1; then
    echo "✅ OK"
    echo "Detalles:"
    curl -s http://localhost:80/health | python3 -m json.tool
else
    echo "❌ FAIL"
fi

# Verificar home
echo -n "Home: "
if curl -f http://localhost:80/ > /dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ FAIL"
fi

echo "=============================="
echo "✅ Verificación completada"
