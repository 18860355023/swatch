from datetime import datetime
from sqlalchemy import create_engine, Column, DateTime, String, pool, Integer, Text, JSON, Boolean, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import PG_DB_HOST,PG_DB_PORT,PG_DB_USER,PG_DBPASSWORD,PG_DB_NAME


# PostgreSQL数据库连接配置
DATABASE_URL = f"postgresql://{PG_DB_USER}:{PG_DBPASSWORD}@{PG_DB_HOST}:{PG_DB_PORT}/{PG_DB_NAME}"

pool_args = {
    'pool_size': 15,  # 连接池中的最大连接数
    'max_overflow': 2,  # 允许超出连接池大小的最大连接数
    'pool_timeout': 5,  # 等待连接的超时时间（秒）
    'pool_recycle': 3600,  # 连接池中的连接在多久之后回收（秒）
}

# 创建数据库引擎并指定连接池参数
engine = create_engine(DATABASE_URL, poolclass=pool.QueuePool, pool_pre_ping=True, **pool_args)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# 数据表的基类（定义表结构用）
Base = declarative_base()

# 所有model的顶层父类，封装公共属性方法
class BaseModel(Base):
    __abstract__ = True
    createdTime =  Column(DateTime, name="created_time", key="createdTime", default=datetime.now, comment="创建时间")
    updatedTime = Column(DateTime, name="updated_time", key="updatedTime",  default=datetime.now, onupdate=datetime.now, comment="更新时间")
    deletedTime = Column(Integer, name="deleted_time", key="deletedTime",  default=0, comment="删除时间")
    # createBy =  Column(String(64), name="create_by", key="createBy", default="admin", nullable=True, comment="创建者")
    # updateBy = Column(String(64), name="update_by", key="updateBy",  default="admin", nullable=True, comment="更新者")
    # version = Column(String(64),name="version",default="0.1.0", nullable=False, comment="版本")

    def to_dict(self):
        # 将model实例转为字典
        model_dict = self.__dict__
        del model_dict['_sa_instance_state']
        model_dict["createdTime"] = model_dict["createdTime"].strftime("%Y-%m-%d %H:%M:%S")
        model_dict["updatedTime"] = model_dict["updatedTime"].strftime("%Y-%m-%d %H:%M:%S")
        return model_dict

    @classmethod
    def comment_key_dict(self):
        return {c.comment: c.key for c in self.__table__.columns if c.comment }
    

# 接口调用日志表模型
class APICallLog(BaseModel):
    __tablename__ = 'api_call_logs'
    __table_args__ = {'comment': '接口日志'}

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String, comment="HTTP方法")
    path = Column(String, comment="请求路径")
    client_ip = Column(String, comment="客户端IP地址")
    status_code = Column(Integer, comment="响应状态码")
    request_body = Column(Text, comment="请求体内容")
    response_body = Column(Text, comment="响应体内容")
    user_agent = Column(String, comment="用户代理")
    # created_at = Column(DateTime, default=datetime.utcnow, comment="日志记录创建时间")


# 原始报文存储表模型
class Messages(BaseModel):
    __tablename__ = 'messages'
    __table_args__ = {'comment': '原始报文'}

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    init_message = Column(String, comment="原始报文")
    parse_message = Column(JSON, comment="解析后的报文")
    report_time = Column(String, comment="上报时间")
    msg_type = Column(String, comment="报文类型")

def get_session():
    return SessionLocal()

def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception:
        import traceback
        traceback.print_exc()
    finally:
        db.close()

