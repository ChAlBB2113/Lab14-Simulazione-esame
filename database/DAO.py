from database.DB_connect import DBConnect
from model import Genes, Interactions

class DAO():

    @staticmethod
    def getGeni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select *
                   from genes
                    """
        cursor.execute(query, ())
        for row in cursor:
            result.append(Genes.Gene(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select g.Chromosome as c
                    from genes g 
                    where g.Chromosome!=0
                    group by g.Chromosome
                            """
        cursor.execute(query, ())
        c=0
        for row in cursor:
            result.append(row["c"])
            c+=1
            print(c)
        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = '''select g1.Chromosome as c1, g2.Chromosome as c2
                    from genes g1, genes g2, interactions i
                    where  g1.GeneID=i.GeneID1  
                           and g2.GeneID=i.GeneID2
                           and g1.Chromosome!=g2.Chromosome
                           and g1.Chromosome!=0
                           and g2.Chromosome!=0
                           
                '''
        cursor.execute(query, ())

        for row in cursor:
            if (row["c1"],row["c2"]) not in result:
                result.append((row["c1"],row["c2"]))

        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getArcoPesato(a):
        conn = DBConnect.get_connection()
        result=[]
        cursor = conn.cursor(dictionary=True)
        query = """select tt.c1, tt.c2, sum(e) as peso
                    from (
                                select  *
                                from(	select g1.Chromosome as c1, g2.Chromosome as c2, i.GeneID1 as g1 , i.GeneID2 as g2 , i.Expression_Corr as e
                                        from genes g1, genes g2, interactions i
                                        where          g1.GeneID=i.GeneID1
                                                       and g2.GeneID=i.GeneID2
                                                       and g1.Chromosome!=0 
                                                       and g2.Chromosome!=0
                                                       and g1.Chromosome!=g2.Chromosome
                                                       and g1.Chromosome=%s
                                                       and g2.Chromosome=%s
                                    ) as t
                                 group by t.g1, t.g2
                            ) as tt
                    group by tt.c1, tt.c2
                    """

        cursor.execute(query, (a[0],a[1]))

        for row in cursor:
                result.append((row["c1"], row["c2"], row["peso"]))

        cursor.close()
        conn.close()
        return result