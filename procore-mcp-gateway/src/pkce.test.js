import { describe, it, expect } from 'vitest'
import { pkceHelper } from './pkce.js'

describe('pkce helper', () => {
  it('should generate verifier with correct length and charset', async () => {
    const { codeVerifier } = await pkceHelper.generateChallenge()
    
    expect(codeVerifier.length).toBeGreaterThanOrEqual(43)
    expect(codeVerifier.length).toBeLessThanOrEqual(128)
    expect(codeVerifier).toMatch(/^[A-Za-z0-9\-._~]+$/)
  })

  it('should verify challenge correctly', async () => {
    const { codeVerifier, codeChallenge } = await pkceHelper.generateChallenge()
    const isValid = await pkceHelper.verifyChallenge(codeVerifier, codeChallenge)
    
    expect(isValid).toBe(true)
  })

  it('should validate verifier correctly', () => {
    const validVerifier = 'abcdefghijklmnopqrstuvwxyz-._~1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ' // 62 chars
    expect(pkceHelper.isValidVerifier(validVerifier)).toBe(true)
    expect(pkceHelper.isValidVerifier('ab')).toBe(false)
    expect(pkceHelper.isValidVerifier('abc@123')).toBe(false)
  })
})