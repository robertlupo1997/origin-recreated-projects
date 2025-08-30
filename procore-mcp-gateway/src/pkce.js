import crypto from 'crypto';

function base64URLEncode(str) {
  return str
    .toString('base64')
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
}

function sha256(buffer) {
  return crypto.createHash('sha256').update(buffer).digest();
}

export const pkceHelper = {
  generateChallenge: async () => {
    const codeVerifier = base64URLEncode(crypto.randomBytes(32));
    const codeChallenge = base64URLEncode(sha256(codeVerifier));
    return { codeVerifier, codeChallenge };
  },

  verifyChallenge: async (codeVerifier, codeChallenge) => {
    const expectedChallenge = base64URLEncode(sha256(codeVerifier));
    return expectedChallenge === codeChallenge;
  },

  isValidVerifier: (verifier) => {
    return verifier && verifier.length >= 43 && verifier.length <= 128 &&
           /^[A-Za-z0-9\-._~]+$/.test(verifier);
  }
};