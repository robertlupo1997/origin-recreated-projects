import { test } from 'node:test';
import assert from 'node:assert';
import { pkceHelper } from './pkce.js';

test('PKCE verifier should have correct length and charset', async () => {
  const { codeVerifier } = await pkceHelper.generateChallenge();
  
  assert(codeVerifier.length >= 43, 'Code verifier should be at least 43 characters');
  assert(codeVerifier.length <= 128, 'Code verifier should be at most 128 characters');
  assert(/^[A-Za-z0-9\-._~]+$/.test(codeVerifier), 'Code verifier should contain only allowed characters');
});

test('PKCE challenge verification should work', async () => {
  const { codeVerifier, codeChallenge } = await pkceHelper.generateChallenge();
  const isValid = await pkceHelper.verifyChallenge(codeVerifier, codeChallenge);
  
  assert(isValid === true, 'Generated challenge should verify correctly');
});

test('PKCE verifier validation should work', () => {
  const validVerifier = 'abcdefghijklmnopqrstuvwxyz-._~1234567890ABCDEFG'; // 50 chars
  assert(pkceHelper.isValidVerifier(validVerifier) === true, 'Valid verifier should pass');
  assert(pkceHelper.isValidVerifier('ab') === false, 'Too short verifier should fail');
  assert(pkceHelper.isValidVerifier('abc@123') === false, 'Invalid character should fail');
});