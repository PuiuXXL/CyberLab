export type Lab = {
  id: number
  name: string
  category: string | null
  description: string | null
}
export type User = { id: number; username: string }

export async function login(username: string): Promise<User> {
  const response = await fetch('/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username }),
  })

  if (response.status === 404) throw new Error('Utilizatorul nu există.')
  if (!response.ok) throw new Error('Nu am putut verifica utilizatorul.')

  return response.json()
}

export async function getLabs(): Promise<Lab[]> {
  const response = await fetch('/api/labs')

  if (!response.ok) throw new Error('Nu am putut încărca laboratoarele.')

  return response.json()
}
