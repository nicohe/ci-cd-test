#!/bin/bash
# Script para ver los logs recientes de todos los servicios

echo "📋 LOGS DE SERVICIOS"
echo "===================="
echo ""

echo "📱 APP LOGS (últimas 20 líneas):"
echo "-----------------------------------"
docker compose logs app --tail=20
echo ""

echo "🌐 NGINX LOGS (últimas 10 líneas):"
echo "-----------------------------------"
docker compose logs nginx --tail=10
echo ""

echo "🐘 POSTGRES LOGS (últimas 5 líneas):"
echo "-----------------------------------"
docker compose logs postgres --tail=5
echo ""

echo "🔴 REDIS LOGS (últimas 5 líneas):"
echo "-----------------------------------"
docker compose logs redis --tail=5
echo ""

echo "===================="
echo "✅ Logs completados"
