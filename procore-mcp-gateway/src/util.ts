export function pkceVerifier(length = 43) {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~'
  let out = ''
  for (let i=0;i<length;i++) out += chars[Math.floor(Math.random()*chars.length)]
  return out
}

export function pkceChallenge(verifier: string): string {
  // Simple base64 encoding simulation for demo
  // Real implementation would use crypto.subtle.digest with SHA256
  const encoder = new TextEncoder()
  const data = encoder.encode(verifier)
  
  // Mock challenge generation (in real implementation, use proper crypto)
  const challenge = Array.from(data)
    .map(b => b.toString(16).padStart(2, '0'))
    .join('')
    .substring(0, 43) // Standard PKCE challenge length
  
  return challenge
}

export function validatePkceParams(verifier: string, challenge: string): boolean {
  return verifier.length >= 43 && 
         verifier.length <= 128 && 
         challenge.length >= 43 && 
         /^[A-Za-z0-9\-._~]+$/.test(verifier)
}
