export default {
    type: "postgres",
    url: process.env.DATABASE_URL,
    ssl: {
        rejectUnauthorized: false
    },
    entities: [
        "./src/entities/*.ts"
    ],
    synchronize: false,
    logging: false, // desabilitar logs em produção
    pool: {
        max: 20, // aumentar pool para múltiplos usuários
        min: 5,
        idle: 10000
    },
    cache: {
        duration: 60000 // cache de 1 minuto para consultas frequentes
    }
}
