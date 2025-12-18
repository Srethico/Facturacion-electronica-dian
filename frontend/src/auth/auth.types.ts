export interface User {
  email: string
  role: string
}

export interface AuthContextType {
  user: User | null
  login: (email: string, password: string) => Promise<void>
  logout: () => void
}