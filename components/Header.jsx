import styles from '../styles/Header.module.css'

export default function Header({ }) {
  return (
    <nav className={styles.nav}>
      <div className={styles.logo}>
        <a href="#">
          <img src="/logo.png" alt="logo" />
        </a>
      </div>
      <div className={styles['menu-items']}>
        <a href="#">snake & ladder</a>
      </div>
    </nav>
  )
}