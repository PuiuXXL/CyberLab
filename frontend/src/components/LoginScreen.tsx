import { useRef, useState } from 'react'
import type { FormEvent } from 'react'
import { BinaryBackground } from './BinaryBackground'

type Props = {
  onLogin: (username: string) => Promise<void>
}

export function LoginScreen({ onLogin }: Props) {
  const [username, setUsername] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const submitting = useRef(false)

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const name = username.trim()
    if (!name || submitting.current) return

    submitting.current = true
    setLoading(true)
    setError('')

    try {
      await onLogin(name)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'A apărut o eroare.')
    } finally {
      submitting.current = false
      setLoading(false)
    }
  }

  return (
    <main className="login-screen">
      <BinaryBackground />
      <div className="login-content">
        <h1 className="login-title">Cyber <span>Lab</span></h1>
        <form className="login-card" onSubmit={handleSubmit} aria-busy={loading}>
          <label htmlFor="username">Nume de utilizator</label>
          <input
            id="username"
            name="username"
            value={username}
            onChange={(event) => setUsername(event.target.value)}
            autoComplete="username"
            maxLength={100}
            readOnly={loading}
            required
          />
          <button type="submit" disabled={loading || username.trim() === ''}>
            {loading ? 'Se încarcă…' : 'Continuă'}
          </button>
          {error && <p className="form-error" role="alert">{error}</p>}
        </form>
      </div>
    </main>
  )
}
