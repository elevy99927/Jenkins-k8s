
SUBDOMAIN=n8n
DOMAIN_NAME=127.0.0.1.nip.io
# -e 

docker run -it --rm  --name n8n  \
	-e N8N_HOST=${SUBDOMAIN}.${DOMAIN_NAME} \
	-e N8N_PORT=5678 \
	-e N8N_PROTOCOL=https \
	-e NODE_ENV=production \
	-e WEBHOOK_URL=https://${SUBDOMAIN}.${DOMAIN_NAME}/ \
	-p 5678:5678  -v n8n_data:/home/node/.n8n  docker.n8n.io/n8nio/n8n


