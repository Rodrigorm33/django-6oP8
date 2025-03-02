import { Entity, Column, PrimaryGeneratedColumn, Index } from "typeorm";

@Entity('infracoes')
export class Infracao {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Index() // index para otimizar busca
    @Column()
    codigo: string;

    @Index() // index para busca por palavras-chave
    @Column()
    descricao: string;

    @Column('decimal', { precision: 10, scale: 2 })
    valor: number;

    @Column()
    pontos: number;

    @Index() // facilitar busca por termos
    @Column({ nullable: true })
    palavrasChave: string;
}
