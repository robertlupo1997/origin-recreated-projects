import { describe, it, expect } from 'vitest'
import { pkceVerifier } from '../src/util'
describe('pkceVerifier', () => {
  it('length and charset', () => {
    const v = pkceVerifier(50)
    expect(v.length).toBe(50)
    expect(/^[A-Za-z0-9\-._~]+$/.test(v)).toBe(true)
  })
})
