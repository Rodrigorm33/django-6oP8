import { getRepository } from "typeorm";
import { Infracao } from "../entities/Infracao";

export class InfracaoService {
    private repository = getRepository(Infracao);

    async buscar(termo: string) {
        return this.repository.createQueryBuilder("infracao")
            .where("infracao.codigo ILIKE :termo", { termo: `%${termo}%` })
            .orWhere("infracao.descricao ILIKE :termo", { termo: `%${termo}%` })
            .orWhere("infracao.palavrasChave ILIKE :termo", { termo: `%${termo}%` })
            .cache(60000)
            .getMany();
    }

    async buscarPorCodigo(codigo: string) {
        return this.repository.findOne({
            where: { codigo },
            cache: true
        });
    }
}
