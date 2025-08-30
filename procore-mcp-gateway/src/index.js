import { Hono } from 'hono';
import { pkceHelper } from './pkce.js';
import { projectsHandler, documentsHandler } from './tools.js';

const app = new Hono();

app.get('/health', (c) => {
  return c.json({ status: 'healthy', service: 'mcp-gateway', version: '0.1.0' });
});

app.post('/auth/pkce/challenge', async (c) => {
  const { codeVerifier, codeChallenge } = await pkceHelper.generateChallenge();
  return c.json({ 
    code_verifier: codeVerifier, 
    code_challenge: codeChallenge,
    code_challenge_method: 'S256'
  });
});

app.post('/auth/pkce/verify', async (c) => {
  const { codeVerifier, codeChallenge } = await c.req.json();
  const isValid = await pkceHelper.verifyChallenge(codeVerifier, codeChallenge);
  return c.json({ valid: isValid });
});

app.get('/tools/projects', projectsHandler);
app.get('/tools/documents', documentsHandler);

const port = process.env.PORT || 3000;

console.log(`MCP Gateway running on port ${port}`);

export default {
  port,
  fetch: app.fetch,
};